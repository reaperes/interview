# Presentational vs container component
* from Dan Abramov
Presentational component is...
```
Are concerned with how things look.
May contain both presentational and container components** inside, and usually have some DOM markup and styles of their own.
Often allow containment via this.props.children.
Have no dependencies on the rest of the app, such as Flux actions or stores.
Don’t specify how the data is loaded or mutated.
Receive data and callbacks exclusively via props.
Rarely have their own state (when they do, it’s UI state rather than data).
Are written as functional components unless they need state, lifecycle hooks, or performance optimizations.
Examples: Page, Sidebar, Story, UserInfo, List.
```

Container component is...
```
Are concerned with how things work.
May contain both presentational and container components** inside but usually don’t have any DOM markup of their own except for some wrapping divs, and never have any styles.
Provide the data and behavior to presentational or other container components.
Call Flux actions and provide these as callbacks to the presentational components.
Are often stateful, as they tend to serve as data sources.
Are usually generated using higher order components such as connect() from React Redux, createContainer() from Relay, or Container.create() from Flux Utils, rather than written by hand.
Examples: UserPage, FollowersSidebar, StoryContainer, FollowedUserList.
```

My point of view (I hate complexity)
* Pure and only work for presentation component is Presentational component.
* Dirty and work for other things - http, communitcation with others, e.t.c. - component is Container component.
