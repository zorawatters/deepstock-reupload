<template>
  <div class="container">
    <p>
      {{date}}<br>
      {{time}}
    </p>
   <b-card img-src="https://placekitten.com/300/300" img-alt="Card image" img-left class="mb-3">
     <b-card-text>
       Some quick example text to build on the card and make up the bulk of the card's content.
       {{intraday}}
     </b-card-text>
   </b-card>
   <b-row class="shadow-lg p-3 mb-5 bg-white rounded col-sm">
     <main-card title="Main Graph">Content</main-card>
     <main-card title="Main Graph">{{msg}}</main-card>
     <main-card title="Main Graph"></main-card>
     <main-card title="Main Graph">Content</main-card>
     <main-card title="Main Graph">Content</main-card>
     <main-card title="Main Graph">Content</main-card>
     <p>Data goes here:</p>

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
    intraday: [],
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
  	let url = window.location.href
  	let re = /[0-9]{2,3}\.[0-9]{2,3}\.[0-9]{2,3}\.[0-9]{2,3}/
  	let domain = url.match(re)[0]
  	console.log(domain)
  	this.msg2 = (await axios.get('http://'+domain+':5000/message')).data
    this.intraday = (await this.$http.get(this.$backendUrl + '/TSLA/intraday')).data
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
