<template>
  <div class="container">
    <b-row class="p-3 mb-2">
      <div class="offset-lg-1 offset-md-1"></div>
      <main-card title="Stock" custom ="card shadow col-lg-7 col-md-7 col-sm-10 p-1">
        <stock-card custom="bg-secondary"></stock-card>
      </main-card>
      <div class="offset-sm-1"></div>
      <main-card title="Toggle" custom ="card shadow col-lg-3 col-md-3 col-sm-10 p-1">
        <toggle-card custom = "bg-warning rounded"></toggle-card>
        <toggle-card custom = "bg-success rounded"></toggle-card>
        <toggle-card custom = "bg-danger rounded"></toggle-card>
        <toggle-card custom = "bg-info rounded"></toggle-card>
      </main-card>
    </b-row>
    <b-row class="p-3 mb-5">
      <div class="offset-lg-1"></div>
      <main-card title="Twitter Card" custom ="card shadow col-lg-5 col-md-6 col-sm-6 p-1 "><twitter-card custom = "bg-secondary"></twitter-card></main-card>
      <main-card title="Sentiment Card" custom ="card shadow col-lg-5 col-md-6 col-sm-6 p-1 "><sentiment-card custom = "bg-secondary"></sentiment-card></main-card>

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
      hello_stocks: ''
    }
  },
  async mounted(){
    this.hello_stocks = (await this.$http.get(this.$backendUrl + '/message')).data
  }
}
</script>
