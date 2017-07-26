### How many types of memory area on JVM?
* Program counter register
* Stacks - Each thread has a private JVM stack, created at the same time as the thread
* Heap - shared among all Java Virtual Machine threads. All class instances and arrays is allocated. It created on virtual machine start-up.
* Method area - shared among all threads.
* Run time constant pool - string, numeric, class info, field info, e.t.c.
* Native method stack

### What is class loader?
Load java classes into the JVM. There are bootstrap class loader, extension class loader, system class loader, e.t.c.
