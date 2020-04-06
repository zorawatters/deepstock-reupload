<template>
  <div class="about container">
    <h1>Developers</h1>
    <b-row>
      <info-card name="Jake Andrus" github = "JakeAndrus" href="https://github.com/JakeAndrus"/>
    </b-row>
    <b-row>
    <info-card name="Natnael Abraha" github = "natnaelmesfun" href="https://github.com/natnaelmesfun"/>
    </b-row>
    <b-row>
    <info-card name="Zora Watters" github = "zorawatters" href="https://github.com/zorawatters"/>
    </b-row>
    <b-row>
    <info-card name="Oscar Delgado" github = "oscardel13" href="https://github.com/oscardel13"/>
    </b-row>
    <b-row>
    <info-card name="Kyle Faucher" github = "kylefaucher" href="https://github.com/kylefaucher"/>
    </b-row>
    <b-row>
    <info-card name="Keaton Whitehead" github = "keatonjwhitehead" href="https://github.com/keatonjwhitehead"/>
    </b-row>

  </div>
</template>
<script>
  import InfoCard from '@/components/InfoCard.vue'

  export default {
    name: 'about',
    components: {
      'info-card': InfoCard
    }
  }
</script>
