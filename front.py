import streamlit as st
from scrape import scrape_website,split_dom, clean_body,extract_body
from parse import parse_ollama

st.title("AI Web Scraper")
url = st.text_input("Enter website URL: ")

if st.button("Scrape Site"):
    st.write("Scraping the website")

    result = scrape_website(url)
    body_content = extract_body(result)
    cleanned_content = clean_body(body_content)

    st.session_state.dom_content = cleanned_content

    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleanned_content, height=300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content")

            dom_chunks = split_dom(st.session_state.dom_content)
            result = parse_ollama(dom_chunks, parse_description)
            st.write(result)