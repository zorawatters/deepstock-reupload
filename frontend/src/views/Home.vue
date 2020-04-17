<template>
  <div class="container">
    <b-row class="p-3 mb-2">
      <main-card title="Stock Graph" custom ="card shadow col-lg-7 col-md-7 col-sm-10 p-1">
        <stock-card custom=""></stock-card>
      </main-card>
      <main-card title="Toggle" custom ="card shadow col-lg-4 col-md-4 col-sm-10 offset-sm-1 p-1">
        <toggle-card custom = "bg-warning rounded m-2" name = "Twitter" ticker = "TWTR" high = "165" low = "154"></toggle-card>
        <toggle-card custom = "bg-success rounded m-2" name = "Google" ticker = "GOOGL" high = "170" low = "130"></toggle-card>
        <toggle-card custom = "bg-danger rounded m-2" name = "Splunk" ticker = "SPLK" high = "190" low = "185"></toggle-card>
        <toggle-card custom = "bg-info rounded m-2" name = "Tesla" ticker = "TSLA" high = "187" low = "145"></toggle-card>
      </main-card>
    </b-row>
    <b-row class="p-3 mb-5">
      <main-card title="Twitter Card" custom ="card shadow col-lg-5 col-md-6 col-sm-6 p-1 offset-lg-1"><twitter-card custom = "bg-secondary"></twitter-card></main-card>
      <main-card title="Sentiment Card" custom ="card shadow col-lg-5 col-md-6 col-sm-6 p-1 offset-lg-1"><sentiment-card custom = "bg-secondary"></sentiment-card></main-card>

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
