<script>
let data = {
  questionnaires: [
    { id : 1, name : 'Questionnaire 1' },
    { id : 2, name : 'Questionnaire 2' },
    { id : 3, name : 'Questionnaire 3' },
    { id : 4, name : 'Questionnaire 4' },
    { id : 5, name : 'Questionnaire 5' }
  ],
  title: 'Mes Questionnaires',
  newItem: ''
};

export default {
  methods: {
    addQuestionnaires: function () {
    },
    mounted(){
      fetch('http://localhost:5000/Quiz/v1.0/questionnaires')
        .then(response => response.json())
        .then(json => {
          console.log("mounted");
          console.log(json).questionnaires;
          this.questionnaires = json.questionnaires;
        })
    }
  },
  components: { QuestionnairesItemItem}
};
</script>

<template>
    {{ questionnaires[1].name }}
</template>