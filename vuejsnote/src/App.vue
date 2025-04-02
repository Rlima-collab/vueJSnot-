<template>
  <div id="app">
    <h1>Gestion des Quiz</h1>
    <button @click="refreshQuestionnaires">Rafraîchir</button>
    <QuestionnaireList :questionnaires="questionnaires" @select="selectQuestionnaire" />
    <QuestionnaireForm :selected-questionnaire="selectedQuestionnaire" @refresh="refreshQuestionnaires" @deselect="deselectQuestionnaire" />
    <div v-if="selectedQuestionnaire">
      <h2>Questions de {{ selectedQuestionnaire.name }}</h2>
      <QuestionList :questions="questions" @select="selectQuestion" />
      <QuestionForm
        :questionnaire-id="selectedQuestionnaire.id"
        :selected-question="selectedQuestion"
        @refresh="refreshQuestions"
      />
    </div>
  </div>
</template>

<script>
import QuestionnaireList from './components/QuestionnaireList.vue';
import QuestionnaireForm from './components/QuestionnaireForm.vue';
import QuestionList from './components/QuestionList.vue';
import QuestionForm from './components/QuestionForm.vue';

export default {
  name: 'App',
  components: {
    QuestionnaireList,
    QuestionnaireForm,
    QuestionList,
    QuestionForm
  },
  data() {
    return {
      questionnaires: [],
      selectedQuestionnaire: null,
      questions: [],
      selectedQuestion: null
    };
  },
  mounted() {
    this.refreshQuestionnaires();
  },
  methods: {
    async refreshQuestionnaires() {
      try {
        const response = await fetch('http://127.0.0.1:5000/questionnaires');
        if (!response.ok) throw new Error('Erreur API');
        const data = await response.json();
        console.log('Questionnaires récupérés:', data);
        this.questionnaires = data.questionnaires || [];
      } catch (error) {
        console.error('Erreur lors du chargement des questionnaires:', error);
      }
    },
    async refreshQuestions() {
      if (this.selectedQuestionnaire) {
        try {
          const response = await fetch(`http://127.0.0.1:5000/questionnaires/${this.selectedQuestionnaire.id}/questions`);
          if (!response.ok) throw new Error('Erreur API');
          const data = await response.json();
          console.log('Questions récupérées:', data);
          this.questions = data.questions || [];
        } catch (error) {
          console.error('Erreur lors du chargement des questions:', error);
        }
      }
    },
    selectQuestionnaire(questionnaire) {
      this.selectedQuestionnaire = questionnaire;
      this.selectedQuestion = null; // Réinitialiser la question sélectionnée
      this.refreshQuestions();
    },
    selectQuestion(question) {
      this.selectedQuestion = question;
    },
    deselectQuestionnaire() {
      this.selectedQuestionnaire = null;
      this.questions = [];
      this.selectedQuestion = null;
    }
  }
};
</script>