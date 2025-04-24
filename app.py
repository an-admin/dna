import streamlit as st
import random

st.set_page_config(page_title="DNA Day Fun App 🎉", page_icon="🧬")

st.title("🎉 Happy DNA Day! 🧬")
st.subheader("Explore the magic in your genes!")

# --- DNA Facts ---
facts = [
    "Your DNA could stretch from the Earth to the sun ~600 times!",
    "You share 98.7% of your DNA with chimpanzees!",
    "Humans have around 20,000-25,000 genes.",
    "If unwound, your DNA in one cell would be 2 meters long.",
    "DNA was discovered in 1869, but its structure wasn't known until 1953!",
    "99.9% of your DNA is the same as every other human being.",
    "The double helix looks like a twisted ladder!",
]

if st.button("🔍 Show me a cool DNA fact!"):
    st.success(random.choice(facts))

# --- DNA Emoji Translator ---
st.markdown("### 🔤 DNA to Emoji Translator")
dna_input = st.text_input("Type a DNA sequence (A, T, G, C):", "ATGC")

emoji_dict = {"A": "🍎", "T": "🌴", "G": "🍇", "C": "🌽"}

if dna_input:
    try:
        translated = "".join(emoji_dict.get(base.upper(), "❓") for base in dna_input)
        st.markdown(f"**Your DNA in emojis:** {translated}")
    except:
        st.error("Something went wrong. Check your sequence!")

# --- DNA Trivia Quiz ---
st.markdown("### 🧠 DNA Trivia")
question = "What is the shape of the DNA molecule?"
options = ["Zigzag line", "Straight ladder", "Double helix", "Triangle"]
answer = "Double helix"

user_answer = st.radio("Choose the correct answer:", options)

if st.button("✅ Submit Answer"):
    if user_answer == answer:
        st.balloons()
        st.success("Correct! 🎉 DNA is a beautiful double helix.")
    else:
        st.error("Oops! Try again. Hint: It's twisted and iconic!")

# --- Genetic Trait Fun ---
st.markdown("### 🎲 Predict a Fun Genetic Trait")
traits = [
    "You probably can't roll your tongue! 👅",
    "You might have a hitchhiker’s thumb! 👍",
    "You might be able to taste bitter foods strongly! 🥦",
    "You might have a longer ring finger than index! ☝️",
    "You likely have a detached earlobe! 👂"
]

if st.button("🎁 What's my fun trait?"):
    st.info(random.choice(traits))

st.markdown("---")
st.caption("Created with ❤️ for DNA Day by Anchit Das")
