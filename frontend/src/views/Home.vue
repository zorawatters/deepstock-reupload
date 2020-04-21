<template>
  <div class="container">
    <b-row class="p-3 mb-2">
      <main-card title="Stock Graph" custom ="card shadow col-lg-7 col-md-7 col-sm-10 p-1" >
        <stock-card custom=""></stock-card>
      </main-card>
      <main-card title="Toggle" custom ="card shadow col-lg-4 col-md-4 col-sm-10 offset-sm-1 p-1">
        <toggle-card custom = "bg-warning rounded mb-2 container shadow" ticker = "AMD" ></toggle-card>
        <toggle-card custom = "bg-success rounded mb-2 container shadow" ticker = "AAPL" @click="$store.commit('setTicker', 'AAPL')"></toggle-card>
        <toggle-card custom = "bg-danger rounded mb-2 container shadow" ticker = "SPLK" @click="$store.commit('setTicker', 'SPLK')"></toggle-card>
        <toggle-card custom = "bg-info rounded  container shadow" ticker = "TSLA" @click="$store.commit('setTicker', 'TSLA')"></toggle-card>
      </main-card>
    </b-row>
    <b-row class="p-3 mb-5">
      <main-card title="Twitter Card" custom ="card shadow col-lg-5 col-md-6 col-sm-6 p-1"><twitter-card></twitter-card></main-card>
      <main-card title="Sentiment Card" custom ="card shadow col-lg-5 col-md-6 col-sm-6 p-1 offset-lg-1"><sentiment-card custom = "bg-secondary" ></sentiment-card></main-card>

    </b-row>
  </div>
</template>

<script>
// @ is an alias to /src
import MainCard from '@/components/MainCard.vue'
import StockCard from '@/components/StockCard.vue'
import TwitterCard from '@/components/TwitterCard.vue'
import ToggleCard from '@/components/ToggleCard.vue'
import SentimentCard from '@/components/SentimentCard.vue'

export default {
  name: 'Home',
  components: {
    'main-card': MainCard,
    'stock-card': StockCard,
    'twitter-card': TwitterCard,
    'toggle-card': ToggleCard,
    'sentiment-card': SentimentCard
  },
  data(){

    return {

    }
  }
}
</script>
