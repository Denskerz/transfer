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
