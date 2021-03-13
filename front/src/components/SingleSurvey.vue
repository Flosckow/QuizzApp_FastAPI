<template>
    <div class="survey">
        <div class="introStage">
            <h1>Welcome to the Quiz: {{title}}</h1>
            <p>
                Some kind of text here. Blah blah.
            </p>

            <button @click="startQuiz">START!</button>
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


    <section class="ab-info-main py-md-5 py-4 editContent single">
        <div class="container py-md-4">
            <div class="row">
                <div class="left-ads-display col-lg-10">
                    <div class="row">
                        <div class="desc1-right col-md-6 pl-lg-4">
                            <h3 class="editContent">{{product.title}}</h3>
                            <ul>
                                <li class="li-movie"><span><b>Описание:</b> {{product.description}}</span>
                                </li>
                                <li class="li-movie"><span><b>Категория:</b>{{product.category}}</span>
                                </li>
                                <li class="li-movie"><span><b>Цена:</b>{{product.price}}</span>
                                </li>
                                <div class="share-desc">
                                    <div class="share">
                                        <ul class="w3layouts_social_list list-unstyled">
                                            <li><button @click="addItemToCart(product)" class="login">Add to Cart</button>
                                                </a>
                                            </li>
                                        </ul>
                                    </div>
                                    <div class="clearfix"></div>
                                </div>
                            </ul>
                        </div>
                    </div>
                    <hr>
                </div>
            </div>
        </div>
    </section>
</template>




<script>
    export default {
        name: "SingleSurvey",
        props: ['id'],
        data() {
            return {
                introStage:false,
                questionStage:false,
                resultsStage:false,
                survey: {},
                question: '',
                answer: [],
                result: 0,
                correctQuestion: 0,
                perc: null
            }
        },
        created() {
            this.loadSurvey()
        },
        methods: {
            async loadSurvey() {
                this.product = await fetch(
                    `${this.$store.getters.getServerUrl}blog/survey/${this.id}`
                ).then(response => response.json())
            },
            startQuiz() {
                this.introStage = false;
                this.questionStage = true;
                console.log()
            },
            handleAnswer(e) {
                console.log('answer event ftw', e)
                this.answer[this.currentQuestion]= e.answer
                if((this.currentQuestion+1) === this.questions.lenght) {
                    this.handleResults()
                    this.questionStage = false
                    this.resultsStage = true
                } else {
                    this.currentQuestion++;
                }
            },
            handleResult() {
                console.log('handle results')
                this.questions.forEach((a, index) => {
                if (this.answer[index] === a.answer) this.correct++
                })
               this.perc = ((this.correct / this.questions.lenght)*100).toFixed(2)
                console.log(this.correct+' '+this.perc)
            },
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