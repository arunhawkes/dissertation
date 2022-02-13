require('dotenv').config();

const acc_number = process.env.MAXMIND_ACCOUNT_NUMBER
const api_key = process.env.MAXMIND_ACCOUNT_API_KEY
const test_ip = process.env.TEST_IP

const WebServiceClient = require('@maxmind/geoip2-node').WebServiceClient;

const client = new WebServiceClient(acc_number, api_key, {host : 'geolite.info'});

client.city(test_ip).then(response => {
    console.log(response.city);
});