<template>
  <div class="card shadow col-lg-3 m-1 p-1">
      <div class="card-body">
        <h4 class="card-title">{{name}}</h4>
        <p class="card-text">{{bio}}</p>
        <a v-bind:href="href" class="btn btn-primary">{{github}}</a>
      </div>
      <!-- <img class="card-img-bottom" v-bind:src="image" v-bind:alt="name" style="width:100%"> -->
      <img class="card-img-bottom" src="../assets/imgs/img_avatar1.png" v-bind:alt="name" style="width:100%">
  <div class="card-transparent text-light shadow-lg col-lg-3 m-3 p-2 bg-gradient-dark" >
      <div class="card-body">
        <h4 class="card-title" style="color: #42b983;">{{name}}</h4>
        <p class="card-text">{{bio}}</p>
        <a v-bind:href="href" class="btn bg-dark text-light" style="color: #42b983;" >{{github}}</a>
      </div>
      <div style="border-color:#42b983; border-style: solid; height:100px; width:100px;" class="rounded-circle center"></div>
      <!-- <img class="card-img-bottom" :src="image" :alt="name" style="width:100%"> -->
  </div>
</template>
<script>

export default {
  name: 'info-card-2',
  props: {
    name: {
      type: String,
      default: ''
    },
    image: {
      type:String,
      type: String,
      default: ""
    },
    github:{
      type: String,
      default: ''
    },
    about:{
      type:String,
      type: String,
      default: ''
    },
    href:{
      type:String,
      default: ''
    },
    bio: {
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
