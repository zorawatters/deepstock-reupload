<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>{{ msg2 }}</h2>
    <p>
      {{date}}<br>
      {{time}}
      </p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data () {
  	return {
  		msg2: 'test'
  	}
  },
  async mounted(){
  	let url = window.location.href
  	let re = /[0-9]{2,3}\.[0-9]{2,3}\.[0-9]{2,3}\.[0-9]{2,3}/
  	let domain = url.match(re)[0]
  	console.log(domain)
  	this.msg2 = (await axios.get('http://'+domain+':5000/message')).data
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
