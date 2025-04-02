<template>
    <div class="question-form">
      <input type="hidden" v-model="id" />
      <label>Titre :</label>
      <input type="text" v-model="title" placeholder="Titre de la question" />
      <label>Type :</label>
      <input type="text" v-model="type" placeholder="Type de la question" />
      <button @click="save" :disabled="!title || !type">Sauvegarder</button>
      <button @click="update" :disabled="!id || !title || !type">Modifier</button>
      <button @click="delete" :disabled="!id">Supprimer</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'QuestionForm',
    props: {
      questionnaireId: {
        type: String,
        required: true
      },
      selectedQuestion: {
        type: Object,
        default: null
      }
    },
    data() {
      return {
        id: '',
        title: '',
        type: ''
      };
    },
    watch: {
      selectedQuestion(newVal) {
        if (newVal) {
          this.id = newVal.id;
          this.title = newVal.title;
          this.type = newVal.question_type;
        } else {
          this.id = '';
          this.title = '';
          this.type = '';
        }
      }
    },
    methods: {
      async save() {
        console.log('Tentative de sauvegarde de la question:', this.title, this.type);
        try {
          const response = await fetch(`http://127.0.0.1:5000/questionnaires/${this.questionnaireId}/questions`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title: this.title, question_type: this.type })
          });
          console.log('Réponse brute:', response);
          if (!response.ok) {
            const errorText = await response.text();
            throw new Error(`Erreur API: ${response.status} - ${errorText}`);
          }
          const data = await response.json();
          console.log('Question créée:', data);
          this.$emit('refresh');
          this.title = '';
          this.type = '';
        } catch (error) {
          console.error('Erreur lors de la sauvegarde:', error);
        }
      },
      async update() {
        console.log('Tentative de modification de la question:', this.id, this.title, this.type);
        try {
          const response = await fetch(
            `http://127.0.0.1:5000/questionnaires/${this.questionnaireId}/questions/${this.id}`,
            {
              method: 'PUT',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({ title: this.title, question_type: this.type })
            }
          );
          if (!response.ok) throw new Error('Erreur API');
          this.$emit('refresh');
        } catch (error) {
          console.error('Erreur lors de la modification:', error);
        }
      },
      async delete() {
        console.log('Tentative de suppression de la question:', this.id);
        try {
          const response = await fetch(
            `http://127.0.0.1:5000/questionnaires/${this.questionnaireId}/questions/${this.id}`,
            {
              method: 'DELETE',
              headers: { 'Content-Type': 'application/json' }
            }
          );
          if (!response.ok) throw new Error('Erreur API');
          this.$emit('refresh');
          this.id = '';
          this.title = '';
          this.type = '';
        } catch (error) {
          console.error('Erreur lors de la suppression:', error);
        }
      }
    }
  };
  </script>