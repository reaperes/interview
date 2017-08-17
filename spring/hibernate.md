# Hibernate
## Cache
### 1st level cache
(Hibernate 1st level cache)[http://howtodoinjava.com/wp-content/uploads/hibernate_first_level_cache.jpg]
* First level cache is associated with “session” object and other session objects in application can not see it.
* The scope of cache objects is of session. Once session is closed, cached objects are gone forever.
* First level cache is enabled by default and you can not disable it.
* When we query an entity first time, it is retrieved from database and stored in first level cache associated with hibernate session.
* If we query same object again with same session object, it will be loaded from cache and no sql query will be executed.
* The loaded entity can be removed from session using evict() method. The next loading of this entity will again make a database call if it has been * removed using evict() method.
* The whole session cache can be removed using clear() method. It will remove all the entities stored in cache.

### 2nd level cache
* See https://docs.jboss.org/hibernate/orm/3.3/reference/en/html/performance.html#performance-cache
