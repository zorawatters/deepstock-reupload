<template>
  <div class="dashboard shadow-lg p-3 mb-5 bg-white rounded">
    <HelloWorld msg="Dashboard"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/Dashboard.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld
  }
}
</script>
