import test from '@/components/test'
import Home from '@/components/HelloFromVux'
import topic from '@/components/topic'

export default {
  routes: [
    {
      path: '/',
      name: 'hello',
      component: Home
    },
    {
      path: '/test',
      name: 'test',
      component: test
    },
    {
      path: '/topic',
      name: 'topic',
      component: topic
    }
  ]
}
