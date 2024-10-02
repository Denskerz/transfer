pipeline {
    agent any

    parameters {
        string(name: 'TABLE_NAMES', defaultValue: 'table1', description: 'Enter table names separated by new lines')
    }

    stages {
        stage('Run Ansible Playbook') {
            steps {
                script {
                    // Разделение строк на массив и преобразование в нужный формат
                    def tables = params.TABLE_NAMES.readLines()
                    def tablesString = tables.collect { "\"${it}\"" }.join(', ')
                    
                    // Вызов Ansible Playbook с передачей переменной
                    sh "ansible-playbook playbook.yml -e 'tables=[${tablesString}]'"
                }
            }
        }
    }
}
script {
    def tables = params.TABLE_NAMES.readLines().findAll { it }
    echo "Parsed tables: ${tables}"
    def tablesString = tables.collect { "\"${it}\"" }.join(', ')
    sh "ansible-playbook playbook.yml -e 'tables=[${tablesString}]'"
}

Also:   org.jenkinsci.plugins.workflow.actions.ErrorAction$ErrorId: 76c8f737-8aea-4847-9601-7f3ad70cc15f
hudson.remoting.ProxyException: groovy.lang.MissingMethodException: No signature of method: java.util.ArrayList.collect() is applicable for argument types: (org.codehaus.groovy.runtime.GStringImpl) values: ["null"]
Possible solutions: collect(), collect(), collect(groovy.lang.Closure), collect(groovy.lang.Closure), collect(java.util.Collection, groovy.lang.Closure), collect(java.util.Collection, groovy.lang.Closure)
