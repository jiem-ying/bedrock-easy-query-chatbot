# Bedrock Easy Query Chatbot

A serverless chatbot implementation using Amazon Bedrock and OpenSearch for intelligent querying and data retrieval.

## Project Overview
This project demonstrates how to build an intelligent chatbot using Amazon Bedrock's foundation models combined with OpenSearch for efficient data retrieval. The chatbot can understand natural language queries, process them through Amazon Bedrock, and return relevant information from the connected data sources.

## Architecture
The solution includes:
- Amazon Bedrock for natural language processing
- Amazon OpenSearch for vector search and data storage
- AWS Lambda for serverless compute
- Amazon EC2 for Steampipe server
- Amazon S3 for data storage
- Amazon VPC for network isolation
- AWS IAM for security and access control

## Prerequisites
- AWS Account with access to:
  - Amazon Bedrock
  - Amazon OpenSearch Service
  - AWS Lambda
  - Amazon EC2
  - Amazon S3
  - Amazon VPC
- Python 3.8 or later
- AWS CLI configured with appropriate credentials
- Basic understanding of AWS services and Python programming

## Setup Instructions
1. Clone the repository
```bash
git clone https://github.com/[your-username]/bedrock-easy-query-chatbot.git
cd bedrock-easy-query-chatbot
```
2. Install required dependencies
```
pip install -r requirements.txt
```
3. Configure AWS credentials
```
aws configure
```

4. Follow the Jupyter notebook for step-by-step deployment:

    VPC and networking setup

    OpenSearch domain creation

    Lambda function deployment

    Bedrock agent configuration

    EC2 Steampipe server setup

    S3 bucket creation and data upload

## Project Structure
```
bedrock-easy-query-chatbot/
├── notebooks/
│   └── main.ipynb         # Main implementation notebook
├── src/
│   ├── lambda_function.py # Lambda function code
│   └── utils.py          # Utility functions
├── config/
│   └── config.yaml       # Configuration files
├── requirements.txt      # Python dependencies
└── README.md            # Project documentation
```

## Usage
1. Open the Jupyter notebook in notebooks/main.ipynb

2. Follow the step-by-step instructions to:

    Set up infrastructure
    Configure the chatbot
    Test queries
    Monitor performance

## Cleanup Instructions
To avoid ongoing charges, remember to clean up all created resources:
1. Delete OpenSearch domain
2. Terminate EC2 instance
3. Delete Lambda function
4. Remove VPC and related resources
5. Empty and delete S3 bucket
6. Delete Bedrock agent and knowledge base
7. Remove IAM roles and policies
Detailed cleanup instructions are provided in the notebook.

## Security Considerations
All services are deployed within a VPC for network isolation
IAM roles follow the principle of least privilege
Sensitive data is encrypted at rest and in transit
VPC endpoints are used for secure service access
## Limitations
Currently supports only English language queries
Requires AWS regions where Bedrock is available
Limited to specific data formats for ingestion
## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.<to-do>

## Acknowledgments
    Amazon Bedrock team for the foundation models
    AWS Documentation and example code
    Community contributors and feedback

## Support
For issues and questions, please open an issue in the GitHub repository.

## Disclaimer
This project is for demonstration purposes and should be properly reviewed and modified before using in a production environment.