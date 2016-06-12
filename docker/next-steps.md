# What should I do next?

## Immediate objective
* I want to create a VM that hosts two docker containers. One of them will be a mongodb volume and another one will be an ambassador which will accept links from other containers.
  
  I want to automate this so it is ephemeral in the Docker Best Practices sense of the word.

  1. Define the mongodb container
  1. Define the ambassador container
  1. Write a fig script to start the two containers
  1. Write a bash script to start the VM and run the fig script
