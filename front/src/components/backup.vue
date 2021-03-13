<template>

    <section class="ab-info-main py-md-5 py-4 editContent single">
        <div class="container py-md-4">
            <div class="row">
            <button @click="startQuiz">START!</button>
                <div class="left-ads-display col-lg-10">
                    <div class="row">
                        <div class="desc1-right col-md-6 pl-lg-4">
                            <h3 class="editContent">{{poll.title}}</h3>
                            <ul>
                                <li class="li-poll"><span><b>Описание:</b> {{poll.description}}</span>
                                </li>
                            </ul>
                        </div>
                        <div v-if="questionStage">
                            <question
                            :question="questions[currentQuestion]"
                            v-on:answer="handleAnswer"
                            :question-number="currentQuestion+1"
                             ></question>
                        </div>
                        <div v-if="resultsStage">
                            You got {{correct}} right out of {{questions.length}} questions. Your percentage is {{perc}}%.
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: "One_poll_action",
    props: ['id'],
    data() {
        return {
            poll: {},
            introStage:false,
            questionStage:false,
            resultsStage:false,
            question: '',
            answer: [],
            result: 0,
            correctQuestion: 0,
            perc: null
        }
    },
    methods: {
        async loadPoll() {
            this.poll = await fetch(
                `http://127.0.0.1:8000/post/1`
            ).then(response => response.json())
            .then(data => {
            return data})
        },
        startQuiz() {
            this.introStage = false;
            this.questionStage = true;
            console.log()
        },
    },
    created() {
        this.loadPoll()
    }
}
</script>

<style scoped>
    .single {
        outline: none;
        outline-offset: -2px;
        cursor: inherit;
        color: rgb(33, 37, 41);
        font-size: 16px;
        background-color: rgba(0, 0, 0, 0);
        font-family: Lato, sans-serif;
    }
    .li-movie{
        list-style: none;
    }
    .login {
        display: inline-block;
        padding: 10px 15px;
        font-size: 14px;
        cursor: pointer;
        text-align: center;
        text-decoration: none;
        outline: none;
        color: #fff;
        background-color: #dd9475;
        border: none;
        border-radius: 15px;
        box-shadow: 0 9px #999;
        margin-left: 5px;
        margin-right: 5px
    }

    .login:hover {background-color: #bf5830}

    .login:active {
        background-color: #3e8e41;
        box-shadow: 0 5px #666;
        transform: translateY(4px);
    }
</style>