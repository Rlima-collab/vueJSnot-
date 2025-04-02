<template>
    <div class="question-list">
      <ul v-if="questions.length">
        <li v-for="q in questions" :key="q.id">
          <a href="#" @click.prevent="$emit('select', q)">{{ q.title }}</a>
        </li>
      </ul>
      <p v-else>Ce questionnaire n’a pas encore de questions.</p>
    </div>
  </template>
  
  <script>
  export default {
    name: 'QuestionList',
    props: {
      questions: {
        type: Array,
        required: true
      }
    }
  };
  </script>