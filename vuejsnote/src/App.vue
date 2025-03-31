<script>
export default {
  data() {
    return {
      questionnaires: [], // Initialisez avec un tableau vide
      title: 'Mes Questionnaires',
      newItem: ''
    };
  },
  methods: {
    addQuestionnaires: function () {
    }
  },
  mounted() {
    fetch('http://localhost:5000/questionnaires')
      .then(response => {
        if (!response.ok) {
          throw new Error('Erreur lors de la récupération des données');
        }
        return response.json();
      })
      .then(json => {
        console.log("Données récupérées :", json);
        this.questionnaires = json.questionnaires; // Assignez les données récupérées
      })
      .catch(error => {
        console.error("Erreur :", error);
      });
  }
};
</script>

<template>
  <div>
    <h1>{{ title }}</h1>
    <ul>
      <li v-for="questionnaire in questionnaires" :key="questionnaire.id">
        {{ questionnaire.name }}
      </li>
    </ul>
  </div>
</template>