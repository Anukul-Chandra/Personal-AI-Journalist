
# Setup Streamlit app for the frontend interface of the Personal AI Journalist
import streamlit as st

import requests



BACKEND_URL = "http://localhost:8000"  



def main():
    st.title("Personal AI Journalist")
    # intialize session state for user input
    if "topics" not in st.session_state:
        st.session_state.topics = []



# Setup Side Bar for user input
    with st.sidebar:
        st.header("Settings")
        source_type = st.selectbox(
            "Select Source",
            ["both", "news", "reddit"],
            format_func=lambda x: f"🌐 {x.capitalize()}" if x == "news" else f"📂 {x.capitalize()}"
        )


    # Topic Mangement
    st.markdown("#### 📝 Topic Management")
    col1, col2 = st.columns([4, 1])
    with col1:
        new_topic = st.text_input("Enter a topic to analyze",placeholder="e.g. Artificial Intelligence")
    with col2:
        add_disabled = len(st.session_state.topics) >= 5 or not new_topic.strip()

        if st.button("Add Topic ➕", disabled=add_disabled):
            st.session_state.topics.append(new_topic.strip())
            st.rerun()


# Add or remove functionality 
    if st.session_state.topics:
        st.subheader("✅ Selected Topics")
        for i,topic in enumerate(st.session_state.topics):
            
            cols = st.columns([4,1])
            cols[0].write(f"{i+1}. {topic}")

            if cols[1].button("Remove ❌", key=f"remove_{i}"):
                del st.session_state.topics[i]
                st.rerun()



    # Analysis Controls
    st.markdown("#### ⚙️ Analysis Controls")
    st.subheader(" 🎙️ Audio Generation")


def handel_api_error(response):

    """Handel API error response """
    
    try:
        error_details = response.json().get("detail", "unknown error")
        st.error(f"API Error ({response.status_code}) - {error_details}")
    except ValueError:
        st.error(f"Unexpected API error - {response.text}")
    
# User able to write topics and mention sources of interest

# Show Response from the backend


if __name__ == "__main__":
    main()