<template>
    <div class="questionnaire-list">
      <ul v-if="questionnaires.length">
        <li v-for="q in questionnaires" :key="q.id">
          <a href="#" @click.prevent="$emit('select', q)">{{ q.name }}</a>
        </li>
      </ul>
      <p v-else>Aucun questionnaire disponible.</p>
    </div>
  </template>
  
  <script>
  export default {
    name: 'QuestionnaireList',
    props: {
      questionnaires: {
        type: Array,
        required: true
      }
    }
  };
  </script>