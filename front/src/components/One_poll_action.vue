<template>
    <section class="ab-info-main py-md-5 py-4 editContent single">
        <div class="container py-md-4">
            <div class="questionContainer" v-if="questionIndex<poll.questions.length" v-bind:key="questionIndex">

				<h2 class="titleContainer title">{{ poll.questions[questionIndex].q }}</h2>
				<h3 @click="test()">click me!</h3>

				<div class="optionContainer">
					<div class="option" v-for="(response, index) in this.poll.questions[questionIndex].answers" @click="selectOption(index)" :class="{ 'is-selected': userResponses[questionIndex] == index}" :key="index">
						{{ index + 1 | charIndex }}. {{ poll.questions.answers.text }}
					</div>
				</div>

				<footer class="questionFooter">

					<nav class="pagination" role="navigation" aria-label="pagination">

						<a class="button" v-on:click="prev();" :disabled="questionIndex < 1">
                    Back
                  </a>

						<a class="button" :class="(userResponses[questionIndex]==null)?'':'is-active'" v-on:click="next();" :disabled="questionIndex>=poll.questions.length">
                    {{ (userResponses[questionIndex]==null)?'Skip':'Next' }}
                  </a>

					</nav>

				</footer>

			</div>
			<div v-if="questionIndex >= poll.questions.length" v-bind:key="questionIndex" class="quizCompleted has-text-centered">

				<span class="icon">
					<i class="fa" :class="resultPoll()>3?'fa-check-circle-o is-active':'fa-times-circle'"></i>
				</span>

				<p class="subtitle">
					Total score: {{ resultPoll() }} / {{ poll.questions.length }}
				</p>
				<br>
				<a class="button" @click="restart()">restart <i class="fa fa-refresh"></i></a>

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
            resultsStage:false,
            userResponses: Array(1).fill(null),
            questionIndex: 0,
        }
    },
    methods: {
        resultPoll () {
            let score = 0;
            for (let i = 0; i < this.userResponses.length; i++) {
                if (
                    typeof this.poll.questions[i].answers[
                        this.userResponses[i]
                    ] !== "undefined" &&
                    this.poll.questions[i].answers[this.userResponses[i]].correct
                ) {
                    score = score + 1;
                }
            }
            return score;
        },
        selectOption (index) {
            this.$set(this.userResponses, this.questionIndex, index);
        },
        restart () {
            this.questionIndex=0
            this.resultStage=Array(this.poll.questions.length).fill(null);
        },
        next () {
            if (this.questionIndex < this.poll.questions.length) {
                this.questionIndex++;
            }
        },
        prev () {
            if (this.poll.questions.length > 0) this.questionIndex--;
        },
        async loadPoll() {
            this.poll = await fetch(
                `http://127.0.0.1:8000/post/${this.id}`
            ).then(response => response.json())
            .then(data => {
            return data
            })
        },
        test () {
            console.log(this.poll.questions)
            console.log(this.poll.questions.answers)
        },
    },
    created() {
        this.loadPoll()
    },

}
</script>









<style scoped>
.button{
	padding: 0.5rem 1rem;
	border: 1px solid rgba(0,0,0,0.25);
	border-radius: 5rem;
	margin: 0 0.25rem;

	transition:0.3s;

	&:hover{
		cursor: pointer;
		background: #ECEFF1;
		border-color:rgba(0,0,0,0.25);
	}
	&.is-active{
		background: $primary_color;
		color: white;
		border-color: transparent;

		&:hover{
			background: darken($primary_color,10%);

		}
	}
}
.button:hover {
    box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
}
.quizForm {
    display: block;
    white-space: normal;

    height: 100%;
    width: 100%;

    .quizFormContainer {
        height: 100%;
        margin: 15px 18px;

        .field-label {
            text-align: left;
            margin-bottom: 0.5rem;
        }
    }
}
.quizCompleted {
    width: 100%;
    padding: 1rem;
    text-align:center;

    > .icon{
        color: #FF5252;
        font-size: 5rem;

        .is-active{
            color: #00E676;
        }
    }
}
.questionContainer {
    white-space: normal;

    height: 100%;
    width: 100%;
}
.optionContainer {
    margin-top: 12px;
    flex-grow: 1;
}
.option {
    border-radius: 290px;
    padding: 3px 9px;
    margin: 0 18px;
    margin-bottom: 12px;
    transition: $trans_duration;
    cursor: pointer;
    background-color: rgba(0, 0, 0, 0.05);
    color: rgba(0,0,0,0.85);
    border: transparent 1px solid;
}

</style>