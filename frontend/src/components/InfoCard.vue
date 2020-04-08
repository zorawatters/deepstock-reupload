<template>
    <div class="card shadow ">
      <h3>{{name}}</h3>
      <a style="color: #42b983;" v-bind:href="href" >{{github}}</a>
      <slot></slot>

    </div>
</template>
<script>

export default {
  name: 'info-card',
  props: {
    name: {
      type: String,
      default: ''
    },
    image: {

    },
    github:{
      type: String,
      default: ''
    },
    about:{
      type:String,
      default: ''
    },
    href:{
      type:String,
      default: ''
    }
  },
  data(){
    return {
    }
  }
}

</script>
<style scoped>
.card {
  /* border: 2px dashed black; */
  width:200px;
}
</style>
