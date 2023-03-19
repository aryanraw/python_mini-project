import streamlit as st
import os


def save_links_to_file(links, filename):
    with open(filename, 'w') as f:
        for link in links:
            f.write(link + '\n')

def main():
    folder_path_lnput = "./input/links.txt"

    #create folder for input link(s)
    if not os.path.exists(folder_path_lnput):
        os.makedirs(folder_path_lnput)
    st.title("Link Saver")

    # Text input to allow the user to input a list of links
    st.subheader("Enter your links:")
    link_text = st.text_area("Separate links with a new line")

    # Button to save the links to a file
    if st.button("Save Links"):
        # Convert the link text into a list of links
        links = link_text.split('\n')
        # Remove any empty links
        links = [link.strip() for link in links if link.strip()]
        if links:
            # Save the links to a text file
            save_links_to_file(links, "./input/links.txt")
            st.success("Links saved successfully!")
        else:
            st.warning("No links were entered.")

if __name__ == '__main__':
    main()