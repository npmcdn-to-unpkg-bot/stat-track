angular.module('todoApp.controller', [])
  .controller('todoController', ["$scope", function($scope) {
    $scope.header = "What needs to be done";
    $scope.newTask = "";
    $scope.taskList = [
      {
        description: "Buy airplane tickets", done:false
      },
      {
        description: "Make hotel reservations", done:false
      },
      {
        description: "Chill", done:false
      }
    ];
    $scope.addTodo = function() {
      $scope.taskList.push({description: $scope.newTask, done:false});
      $scope.newTask = "";
    }
    $scope.delete = function(index) {
      $scope.taskList.splice(index, 1);
      $scope.newTask = "";
    }
  }]);
