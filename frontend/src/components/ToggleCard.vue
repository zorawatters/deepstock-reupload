<template>
<div :class = "custom">
  <p>Toggle Card</p>
</div>
</template>
<script>

  export default {
    name: 'toggle-card',
    props: {
      custom: {
        type: String,
        default: ''
      },
    },
    data(){
      return {
      }
    }
  }
</script>
