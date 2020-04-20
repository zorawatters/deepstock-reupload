<template>
<div :class = "custom">
  <!-- <p>{{ticker}} - {{name}} <t> <a style="color:28a745"> {{high}} </a>|<a style="color:dc3545"> {{low}} </a></p> -->
    <p> <a style = "color:dc3545">{{ticker}}</a> {{name}} {{high}} {{low}} </p>
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
      name: {
        type: String,
        default: ''
      },
      ticker: {
        type: String,
        default: ''
      },
      high:{
        type: String,
        default: ''
      },
      low: {
        type: String,
        default: ''
      }
    },
    data(){
      return {
      }
    }
  }
</script>
