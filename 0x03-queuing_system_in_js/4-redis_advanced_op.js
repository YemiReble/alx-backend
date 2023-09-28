import { createClient } from 'redis';

const client = await createClient();

client.on('error', (err) => console.log('Redis client not connected to the server:', err));

client.connect();
  
client.on('success', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
    const value = client.get(schoolName);
    
    return value;
}

client.disconnect();


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
