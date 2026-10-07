import streamlit as st

st.set_page_config(page_title="Timotee SS3B AI", page_icon="🧠", layout="centered")

# Try to show logo if you uploaded logo.png
try:
    st.image("logo.png", width=120)
except:
    st.markdown("## 🧠 Timôteé däl Ai")

st.title("Timôteé däl Ai")
st.subheader("By Okoye Timothy | SS3B | Computer Studies Project")
st.markdown("---")

st.header("📚 Research Article: Computer Networking")
st.caption("Assignment: Not more than 2 pages | Importance: Resource Sharing, Communication, Collaboration")

article = """
COMPUTER NETWORKING - AN OVERVIEW

1. WHAT IS COMPUTER NETWORKING?
Computer Networking is the practice of connecting two or more computers together to share resources and exchange information. These computers are connected using cables (wired) or wireless signals like Wi-Fi and Bluetooth.

2. IMPORTANCE OF COMPUTER NETWORKING

a) RESOURCE SHARING:
Networking allows many users to share one resource. For example, in our school computer lab, many computers can share one printer, one internet connection, and one set of files. This saves money and time. Instead of buying a printer for every computer, we buy one network printer.

b) COMMUNICATION:
Networking makes communication very fast and easy. People can send emails, chat on WhatsApp, make video calls, and share messages instantly across the world. Without networking, we cannot use Facebook, Instagram, Opay or WhatsApp.

c) COLLABORATION:
Collaboration means working together. With networking, many students can work on one document at the same time using Google Docs. Workers in an office can work together on one project from different places. This improves teamwork.

3. PRACTICAL EXAMPLES OF COMPUTER NETWORKING

1. School LAN (Local Area Network): All computers in our school ICT lab connected to one router and sharing files.

2. Internet as WAN (Wide Area Network): The biggest network in the world that connects all schools, banks and phones together.

3. Bluetooth PAN (Personal Area Network): Connecting my phone to a Bluetooth speaker or sharing files from phone to laptop.

4. Opay/Online Banking Network: When we send money, our phone connects to the bank network to transfer money.

5. Google Docs Collaboration: SS3B students can type our Computer assignment together online at the same time from different homes.

CONCLUSION:
Computer networking has made life easier by allowing us to share resources, communicate faster and collaborate better. It is the foundation of the modern internet and digital world.

Written by: Okoye Timothy, SS3B
School: Computer Studies Assignment
"""

st.write(article)

st.markdown("---")
st.success("✅ Assignment completed - Covers Meaning, Importance and 5 Practical Examples")

# DOWNLOAD BUTTONS - FOR TEACHER AND CLASSMATES
st.subheader("📥 Download Your Article")

txt_file = article

st.download_button(
    label="Download as TXT (For Phone)",
    data=txt_file,
    file_name="Okoye_Timothy_SS3B_Computer_Networking.txt",
    mime="text/plain"
)

st.download_button(
    label="Download as DOC (For Submission)",
    data=txt_file,
    file_name="Okoye_Timothy_SS3B_Computer_Networking.doc",
    mime="text/plain"
)

st.markdown("---")
st.info("Share this link to your teacher: This AI hosts your SS3 assignment with download option.")

st.markdown("### 🤖 Ask Timôteé däl Ai Anything")
user_q = st.text_input("Type your question about Networking:")
if user_q:
    q = user_q.lower()
    if "network" in q:
        st.write("Computer Networking is connecting computers to share resources, communicate and collaborate. Example is School LAN.")
    elif "resource" in q:
        st.write("Resource Sharing means many computers sharing one printer, one internet, one file. It saves cost.")
    elif "communication" in q:
        st.write("Networking helps us chat, email and video call. Like WhatsApp and Facebook use network.")
    elif "collaboration" in q:
        st.write("Collaboration is working together. Like many students editing one Google Docs at same time.")
    elif "example" in q:
        st.write("5 Examples: 1. School LAN 2. Internet WAN 3. Bluetooth PAN 4. Opay Bank Network 5. Google Docs")
    else:
        st.write("I am Timôteé däl Ai built by Okoye Timothy SS3B. I can explain Resource Sharing, Communication, Collaboration and Networking examples.")