# circleci-paho

https://www.hackster.io/mariocannistra/python-and-paho-for-mqtt-with-aws-iot-921e41
 
aws iot create-thing --thing-name "myThingName"
aws iot list-things
aws iot create-keys-and-certificate --set-as-active --certificate-pem-outfile cert.pem --public-key-outfile publicKey.pem --private-key-outfile privkey.pem
aws iot list-certificates
aws iot create-policy --policy-name "PubSubToAnyTopic" --policy-document file://iotpolicy.json
	"arn:aws:iot:us-west-2:123275298972:cert/7f695125ea81f8b5d0cff3f9ef917d1dd0a2e6ddeb51371630d8f556e83a8a72
iaws iot attach-principal-policy --principal "arn:aws:iot:us-west-2:123275298972:cert/7f695125ea81f8b5d0cff3f9ef917d1dd0a2e6ddeb51371630d8f556e83a8a72" --policy-name "PubSubToAnyTopic"
aws iot attach-thing-principal --thing-name "myThingName" --principal "arn:aws:iot:us-west-2:123275298972:cert/7f695125ea81f8b5d0cff3f9ef917d1dd0a2e6ddeb51371630d8f556e83a8a72"

pip install paho-mqtt
./awsiotpub.py 
./awsiotsub.py 
