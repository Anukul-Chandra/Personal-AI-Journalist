import streamlit as st


def main():
    st.title("Personal AI Journalist")

    # Setup Side Bar for user input
    with st.sidebar:
        st.header("Settings")
        source_type = st.selectbox(
            "Select Source",
            ["both", "news", "reddit"],
            format_func=lambda x: f"🌐 {x.capitalize()}" if x == "news" else f"📂 {x.capitalize()}"
        )

    # User able to write topics and mention sources of interest

    # Show Response from the backend


if __name__ == "__main__":
    main()