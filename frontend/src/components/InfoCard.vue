<template>
    <div class="card-transparent text-light shadow col-lg-3 m-3 p-2 bg-gradient-dark" style="">
      <!-- <img class="card-img-bottom" v-bind:src="image" v-bind:alt="name" style="width:100%"> -->
      <img class="card-img-bottom" :src="image" :alt="name" style="width:100%">
        <div class="card-body">
          <h4 class="card-title"style="color: #42b983;">{{name}}</h4>
          <p class="card-text">{{bio}}</p>
          <a v-bind:href="href" class="btn bg-dark text-light">{{github}}</a>
        </div>
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
      type: String,
      default: ''
    },
    github:{
      type: String,
      default: ''
    },
    about:{
      type: String,
      default: ''
    },
    href:{
      type: String,
      default: ''
    },
    bio: {
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
<style scoped>
.card {

}
</style>
