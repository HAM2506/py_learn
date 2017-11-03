import test from '@/components/test'
import Home from '@/components/HelloFromVux'

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
    }
  ]
}
