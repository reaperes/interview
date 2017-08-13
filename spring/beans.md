# Beans
## Bean scopes
* singleton : Scopes a single bean definition to a single object instance per Spring IoC container.
* prototype : Scopes a single bean definition to any number of object instances.
* request : Scopes a single bean definition to the lifecycle of a single HTTP request
* session : Scopes a single bean definition to the lifecycle of an HTTP Session
* globalSession : Scopes a single bean definition to the lifecycle of a global HTTP Session
* application : Scopes a single bean definition to the lifecycle of a ServletContext
* websocket : Scopes a single bean definition to the lifecycle of a WebSocket

## Bean lifecycle
(http://www.wideskills.com/spring/spring-bean-lifecycle)

1. Instantiate
2. Populate properties
3. BeanNameAware#setBeanName
4. BeanFactoryAware#setBeanFactory
5. ApplicationContextAware#setApplicationContext
6. BeanPostProcessor#postProcessBeforeInitialization
7. InitializingBean#afterPropertiesSet
8. Custom init method
9. BeanPostProcessor#postProcessAfterInitialization
10. READY TO USE
11. DisposableBean#destroy
12. Custom destroy method
