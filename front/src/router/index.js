import Vue from 'vue'
import VueRouter from 'vue-router'
import HelloWorld from '../views/HelloWorld.vue'
import Poll from '../components/Poll.vue'
import Survey from '../components/Survey.vue'
import CreateSurvey from '../components/CreateSurvey.vue'
import CreatePoll from '../components/CreatePoll.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'HelloWorld',
        component: HelloWorld
    },
    {
        path: '/poll/all',
        name: 'Poll',
        component: Poll
    },
    {
        path: '/poll/create',
        name: 'CreatePoll',
        component: CreatePoll
    },
    {
        path: '/survey/all',
        name: 'Survey',
        component: Survey
    },
    {
        path: '/survey/create',
        name: 'CreateSurvey',
        component: CreateSurvey
    }
]

const router = new VueRouter({
    mode: 'history',
    routes
})

export default router
