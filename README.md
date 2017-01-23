# circleci-paho

https://www.hackster.io/mariocannistra/python-and-paho-for-mqtt-with-aws-iot-921e41
 
- aws iot create-thing --thing-name "myThingName"
- aws iot list-things
- aws iot create-keys-and-certificate --set-as-active --certificate-pem-outfile cert.pem --public-key-outfile publicKey.pem --private-key-outfile privkey.pem
- aws iot list-certificates
- aws iot create-policy --policy-name "PubSubToAnyTopic" --policy-document file://iotpolicy.json
	"arn:aws:iot:us-west-2:123275298972:cert/7f695125ea81f8b5d0cff3f9ef917d1dd0a2e6ddeb51371630d8f556e83a8a72
- aws iot attach-principal-policy --principal "arn:aws:iot:us-west-2:123275298972:cert/7f695125ea81f8b5d0cff3f9ef917d1dd0a2e6ddeb51371630d8f556e83a8a72" --policy-name "PubSubToAnyTopic"
- aws iot attach-thing-principal --thing-name "myThingName" --principal "arn:aws:iot:us-west-2:123275298972:cert/7f695125ea81f8b5d0cff3f9ef917d1dd0a2e6ddeb51371630d8f556e83a8a72"

pip install paho-mqtt
./awsiotpub.py 
./awsiotsub.py 

# This worked.... How about this? http://dev.classmethod.jp/cloud/aws-iot-cloudwatch-logs/
- aws iot set-logging-options --logging-options-payload roleArn="arn:aws:iam::123275298972:role/aws_iot_cloudwatch_log",logLevel="INFO"
- aws iot set-logging-options --logging-options-payload roleArn="arn:aws:iam::123275298972:role/aws_iot_cloudwatch_log",logLevel="DISABLED"

# debugging (hmm... not sure if this works.... https://www.hackster.io/bees/aws-iot-and-beehives-c59fff)
- aws iam create-role --role-name "iot-logging-role" --assume-role-policy-document file://iot-logging-role.txt
- aws iam create-policy --policy-name "iot-logging-policy" --policy-document file://iot-logging-policy.txt
- aws iam attach-role-policy --role-name "iot-logging-role" --policy-arn "arn:aws:iam::123275298972:policy/iot-logging-policy"
 
- aws iot set-logging-options --logging-options-payload roleArn="arn:aws:iam::123275298972:role/aws_iot_cloudwatch_log",logLevel="INFO"
- aws iot set-logging-options --logging-options-payload roleArn="arn:aws:iam::123275298972:role/aws_iot_cloudwatch_log",logLevel="DISABLED"
