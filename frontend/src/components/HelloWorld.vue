<template>
  <div class="hello">
   <b-row class="shadow-lg p-3 mb-5 bg-white rounded col-sm">
     <main-card :title="hello_stocks"></main-card>
     <main-card title="Twitter Data"></main-card>
     <main-card title="News Articles"></main-card>
   </b-row>
  </div>
</template>

<script>
import axios from 'axios'
import MainCard from '@/components/MainCard.vue'
export default {
  name: 'HelloWorld',
  props: {
    msg: String,
  },
  components: {
    'main-card': MainCard
  },
  data () {
  	return {
  		msg2: 'This is a test'
  	}
  },
  async mounted(){
  	//let url = window.location.href
  	//let re = /[0-9]{2,3}\.[0-9]{2,3}\.[0-9]{2,3}\.[0-9]{2,3}/
  	//let domain = url.match(re)[0]
  	//console.log(domain)
  	this.hello_stocks = (await this.$http.get(this.$backendUrl + '/message')).data
  },
  methods: {
  	logMsg: function(){
  		console.log(this.msg2);
  	}
  },
  computed: {
  	date: function(){
  		return new Date()
  	},
  	time: function(){
  		return (new Date).getTime()
  	}
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
