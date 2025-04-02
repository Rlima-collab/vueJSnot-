<template>
    <div class="questionnaire-form">
      <input type="hidden" v-model="id" />
      <label>Nom du questionnaire :</label>
      <input type="text" v-model="name" placeholder="Nom du questionnaire" />
      <button @click="save" :disabled="!name">Sauvegarder</button>
      <button @click="update" :disabled="!id || !name">Modifier</button>
      <button @click="delete" :disabled="!id">Supprimer</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'QuestionnaireForm',
    props: {
      selectedQuestionnaire: {
        type: Object,
        default: null
      }
    },
    data() {
      return {
        id: '',
        name: ''
      };
    },
    watch: {
      selectedQuestionnaire(newVal) {
        if (newVal) {
          this.id = newVal.id;
          this.name = newVal.name;
        } else {
          this.id = '';
          this.name = '';
        }
      }
    },
    methods: {
      async save() {
        console.log('Tentative de sauvegarde du questionnaire:', this.name);
        try {
          const response = await fetch('http://127.0.0.1:5000/questionnaires', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name: this.name })
          });
          console.log('Réponse brute:', response);
          if (!response.ok) {
            const errorText = await response.text();
            throw new Error(`Erreur API: ${response.status} - ${errorText}`);
          }
          const data = await response.json();
          console.log('Questionnaire créé:', data);
          this.$emit('refresh');
          this.name = '';
        } catch (error) {
          console.error('Erreur lors de la sauvegarde:', error);
        }
      },
      async update() {
        console.log('Tentative de modification du questionnaire:', this.id, this.name);
        try {
          const response = await fetch(`http://127.0.0.1:5000/questionnaires/${this.id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name: this.name })
          });
          if (!response.ok) throw new Error('Erreur API');
          this.$emit('refresh');
        } catch (error) {
          console.error('Erreur lors de la modification:', error);
        }
      },
      async delete() {
        console.log('Tentative de suppression du questionnaire:', this.id);
        try {
          const response = await fetch(`http://127.0.0.1:5000/questionnaires/${this.id}`, {
            method: 'DELETE',
            headers: { 'Content-Type': 'application/json' }
          });
          if (!response.ok) throw new Error('Erreur API');
          this.$emit('refresh');
          this.id = '';
          this.name = '';
          this.$emit('deselect');
        } catch (error) {
          console.error('Erreur lors de la suppression:', error);
        }
      }
    }
  };
  </script>