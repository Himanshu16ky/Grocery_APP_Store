<template>
  <div>
    <button @click="triggerCeleryTask">Trigger Celery Task</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  methods: {
    async triggerCeleryTask() {
      try {
        const response = await axios.get('/api/trigger_celery'); // Make a GET request to your Flask API endpoint
        console.log('Task ID:', response.data['Task ID']);
        console.log('Task State:', response.data['Task State']);
        console.log('Task Result:', response.data['Task Result']);
      } catch (error) {
        console.error('Error:', error);
      }
    }
  }
}
</script>
