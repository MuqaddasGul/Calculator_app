import streamlit as st
st.markdown("""
<style>
/* All normal text */
.stApp {
    color: white !important;
}
[data-testid="stAppViewContainer"] {
    background: linear-gradient(
        135deg,
        #3B4CCA,
        #7B3FA1,
        #D94F70
    ) !important;
}
.math-symbol {
    position: fixed;
    font-size: 55px;
    font-weight: bold;
    color: rgba(255, 255, 255, 0.12);
    pointer-events: none;
    z-index: 0;
}

.stAppViewContainer .main .block-container {
    position: relative;
    z-index: 1;
}
/* Input label */
label {
    color: white !important;
}

/* Input text */
div[data-baseweb="input"] input {
    color: white !important;
}

/* Input placeholder */
div[data-baseweb="input"] input::placeholder {
    color: #D1D5DB !important;
}

/* Selectbox text */
div[data-baseweb="select"] [role="combobox"] {
    color: white !important;
}

/* Selectbox label */
div[data-baseweb="select"] label {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<div class="math-symbol" style="top: 8%; left: 12%;">π</div>
<div class="math-symbol" style="top: 15%; left: 45%;">√</div>
<div class="math-symbol" style="top: 22%; left: 75%;">Σ</div>
<div class="math-symbol" style="top: 30%; left: 25%;">%</div>
<div class="math-symbol" style="top: 46%; left: 82%;">÷</div>
<div class="math-symbol" style="top: 64%; left: 70%;">×</div>
<div class="math-symbol" style="top: 73%; left: 18%;">=</div>
<div class="math-symbol" style="top: 55%; left: 40%;">−</div>
<div class="math-symbol" style="top: 65%; left: 18%;">∞</div>
<div class="math-symbol" style="top: 82%; left: 55%;">%</div>
<div class="math-symbol" style="top: 78%; left: 48%;">√</div>
<div class="math-symbol" style="top: 46%; left: 82%;">÷</div>
<div class="math-symbol" style="top: 22%; left: 75%;">Σ</div>
<div class="math-symbol" style="top: 38%; left: 60%;">+</div>
""", unsafe_allow_html=True)
if "history" not in st.session_state:
    st.session_state.history = []
st.markdown(
    '<h1 style="color:white;text-align:center;">🧮My calculater<h1>',
    unsafe_allow_html=True
)
st.divider()
numbers=st.text_input(
    "Enter your inputs seperated by commas",
    placeholder="Example 10,20, 30",
    key="user_input"
)
operation= st.selectbox(
    "Choose operation",
    ["Choose operation","Addition", "Subtraction", "Multiplication","Division","Modulus","Floor division" ],
    key="operation"

)
def reset_calculator():
    st.session_state.user_input= ""
    st.session_state.operation = "Choose operation"
def clear_history():
    st.session_state.history = []
    st.session_state.user_input = ""
    st.session_state.operation = "Choose operation"
def add_to_history(calculation):
    if not st.session_state.history or st.session_state.history[-1] != calculation:
        st.session_state.history.append(calculation)

if numbers:
    try:
        nums = [float(x.strip())for x in numbers.split(",")]
        if operation == "Choose operation":
            st.info("please choose an operation")
        elif operation == "Addition":
            result=sum(nums)
            st.success(f"✅Result:{result}")
            add_to_history(f"{numbers} + = {result}")
        elif operation == "Subtraction":
            result=nums[0]
            for num in nums[1:]:
                result -= num
            st.success(f"✅Result:{result}")
            add_to_history(f"{numbers} - = {result}")
        elif operation == "Multiplication":
            result=1
            for num in nums:
                result *=num
            st.success(f"✅Result:{result}")
            add_to_history(f"{numbers} * = {result}")
        elif operation == "Division":
            result=nums[0]
            for num in nums[1:]:
                if num==0:
                    result="cannot divide by zero"
                    break
                result/=num
            st.success(f"✅Result:{result}")
            add_to_history(f"{numbers} / = {result}")
        elif operation == "Modulus":
            result = nums[0]
            for num in nums[1:]:
                if num == 0:
                    st.error("cannot use modulus with 0")
                    break
                result %= num
            else:
                st.success(f"✅Result:{result}")
                add_to_history(f"{numbers} % = {result}")
        elif operation == "Floor division":
            result=nums[0]
            for num in nums[1:]:
                if num == 0:
                    st.error("cannot divide by zero")
                    break
                result //= num
            else:
                st.success(f"✅Result:{result}")
                add_to_history(f"{numbers} // = {result}")  
    except ValueError:
        st.error("🚫Invalid input! Please enter numbers seperated by commas.")
st.button("🔄Reset/Clear",on_click=reset_calculator)
st.markdown(
    '<h2 style="color:#008080;text-align:center;">📜Calculation History</h2>',
    unsafe_allow_html=True
)
if st.session_state.history:
    for item in reversed(st.session_state.history):
        st.write(item)
else:
    st.info("no calculations yet.")
st.button("🚮Clear History", on_click=clear_history)
