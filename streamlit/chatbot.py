import streamlit as st
import boto3
import json
from botocore.response import StreamingBody
import random
import string

region = boto3.Session().region_name
print(region)
session = boto3.Session(region_name=region)
lambda_client = session.client('lambda')

# Function to generate presigned URL for S3 object
def generate_presigned_url(bucket_uri):
    s3 = boto3.client('s3')
    bucket_name, key = bucket_uri.split('/', 2)[-1].split('/', 1)
    print("Bucket name and key:")
    print(bucket_name, key)
    try:
        presigned_url = s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': key},
            ExpiresIn=3600  # URL expires in 1 hour
        )
        return presigned_url
    except ClientError as e:
        st.error(f"Error generating presigned URL: {e}")

st.title("Easy-Query Chatbot using Steampipe for AWS Resources in your account")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to generate a random session ID
def generate_session_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))

# Use Streamlit's session state to store the session ID
if 'sessionId' not in st.session_state:
    st.session_state['sessionId'] = generate_session_id()

# Now you can use st.session_state.session_id throughout your app
print('print my session ID:', st.session_state['sessionId'])

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):

    # Display user input in chat message container
    question = prompt
    st.chat_message("user").markdown(question)

    # Call lambda function to get response from the model
    payload = json.dumps({"question":prompt,"sessionId": st.session_state['sessionId']})
    print(payload)
    result = lambda_client.invoke(
                FunctionName='InvokeEasyQueryAgent',
                Payload=payload
            )

    result = json.loads(result['Payload'].read().decode("utf-8"))
    print(result)

    answer = result['body']['answer']
    sessionId = result['body']['sessionId']
    #Add citations
    citations = result['body']['citations']
    # print(citations)

    st.session_state['sessionId'] = sessionId
    # Add user input to chat history
    st.session_state.messages.append({"role": "user", "content": question})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        display_text = answer
        st.markdown(display_text)
        # Loop over the citations list and display each citation in a separate chat message
        # for citation in citations:

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": answer})

