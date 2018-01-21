import re

class GroomingField(object):
    """
    """
    SplitBlank = ' '*4
    def __init__(self):
        pass 
        
    def add_subfield(self, field, subfield, subfield_default=None):
        """
        add the sub field 
        :param field: dictionary 
        :param subfield: string
        :param subfield_default: string 
        :return field: dictionary 
        """
        field.setdefault(subfield, subfield_default)
        return field
    
    def first_letter_upper(self, orig_string):
        orig_string = ' ' + orig_string
        re_string = re.sub(r'\s+(?P<first>\w)',lambda x:' '+x.group('first').upper(),orig_string)
        return re_string.strip()


    def append_case_keyword_step(self, step_name, *step_args):

        append_str = '\n'+self.SplitBlank + step_name
        for arg in step_args:
            append_str +=self.SplitBlank+arg
        return append_str


class SettingField(GroomingField):
    """
    """

    def __init__(self,documentation='',suitsetup='',suitteardown='',force_tag=''):
        self.setting_content = '*** Setting ***'
        self.setting_field = {'documentation': documentation,
                             'suit_setup': suitsetup,
                             'suit_teardown': suitteardown,
                             'force_tag': force_tag,
                              }
    def generate_setting_field(self):
        self.add_subfield(self.setting_field,'blank',self.SplitBlank)
        self.setting_content += "\nDocumentation%(blank)s%(documentation)s\nSuit SetUp%(blank)s%(suit_setup)s\n"\
                                          "Suit Teardown%(blank)s%(suit_teardown)s\nForce Tag%(blank)s%(force_tag)s" % self.setting_field
        return self.setting_content

    def add_library(self, *args):
        for library in args:
            self.setting_content += '\n'+'library'+self.SplitBlank+library

    def add_resource(self, *args):
        for resource in args:
            self.setting_content += '\n'+'Resource'+self.SplitBlank+resource


class VariableField(GroomingField):
    """
    """

    def __init__(self, **kwagrs):
        self.variable_content = '*** Variable ***'
        self.variable_field = kwagrs

    def generate_variable_field(self):
        for var, value in self.variable_field.items():
            self.variable_content +='\n'+var+self.SplitBlank+value
        return self.variable_content


class TestCaseField(GroomingField):

    """
    case_field = {'casename':'',
                           'tags':'',
                           'setup':'',
                           'teardown':'',
                           'template':'',
                           'timeout':'',
                           'steps':[(step_name,[step_args,])],
                           }
    """

    def __init__(self, case_list=None):
        self.case_content = "*** Test Case ***"
        self.case_list = case_list


    def generate_case_field(self):
        for case in self.case_list:
            self.case_content +='\n'+self.first_letter_upper(case.get('casename',''))
            self.case_content +=self.append_case_keyword_step('[Tags]',case.get('tags','')) 
            self.case_content +=self.append_case_keyword_step('[Setup]',self.first_letter_upper(case.get('setup','')))
            self.case_content +=self.append_case_keyword_step('[Template]', case.get('template',''))
            self.case_content +=self.append_case_keyword_step('[Timeout]', case.get('timeout',''))
            for step in case['steps']:
                self.case_content +=self.append_case_keyword_step(self.first_letter_upper(step[0]),*step[1])
            self.case_content +=self.append_case_keyword_step('[Teardown]',self.first_letter_upper(case.get('teardown','')))
        return self.case_content


class KeywordField(GroomingField):
    """
    """

    def __init__(self, keyword_list=None):
        self.keyword_content = "*** Keyword ***"
        self.keyword_field = {'keywordname':'',
                           'arguments':'',
                           'teardown':'',
                           'returnvalue':'',
                           'timeout':'',
                           'steps':[{'stepname':'',
                                    'stepargs':[]},],
                           }
        self.keyword_list = keyword_list

    

    def generate_keyword_field(self):
        for keyword in self.keyword_list:
            self.keyword_content +='\n'+self.first_letter_upper(keyword.get('keywordname',''))
            self.keyword_content +=self.append_case_keyword_step('[Arguments]',keyword.get('arguments','')) 
            self.keyword_content +=self.append_case_keyword_step('[Timeout]',keyword.get('timeout',''))
            for step in keyword.get('steps',[]):
                self.keyword_content +=self.append_case_keyword_step(self.first_letter_upper(step['stepname']),*step.get('stepargs',[]))
            self.keyword_content +=self.append_case_keyword_step('[Teardown]',self.first_letter_upper(keyword.get('teardown','')))
            self.keyword_content +=self.append_case_keyword_step('[Return]',keyword.get('returnvalue',''))
            
        return self.keyword_content       


class GroomingAtddToRobot(object):
    """
    """


    def __init__(self,grooming_obj, robot_case_name=None):
        self.obj = grooming_obj
        self.robot_case_name = robot_case_name
        self.robot_case_content = ''
        self.case_list = []
        self.parse_grooming_field()

    def parse_grooming_field(self):
        self.content = self.obj.content + ' \n'
        print(self.content)
        self.scope = self.obj.scope
        self.question = self.obj.question
        self.assumption = self.obj.assumption
        if self.robot_case_name is None:
            self.robot_case_name = './robotcase/robotcase_storage/'+\
                                   self.obj.sprint.strip() + '_' +\
                                   self.obj.feature.strip()+'_'+re.sub(r'\s+','_',self.obj.title.strip())+'.robot'

    def generate_cases(self):
        '''\n####Subcase:test\n
                *Precondtion:test\n
                *Operation:test\n
                           test\n
                *Expect Result:test\n
                *Check Point:test\n
            \n####Subcase:test\n
                *Precondtion:test\n
                *Operation:test\n
                           test\n
                *Expect Result:test\n
                *Check Point:test\n'''    
               
        case_list_var = self.content.split('####Subcase:')[1:]
        for case_detail in case_list_var:
            subcase = {'casename':'',
                    'tags':'',
                    'setup':'',
                    'teardown':'',
                    'template':'',
                    'timeout':'',
                    'steps':[('',[])],
                           }

            case_pattern =r'(.+)\s{4}\*Precondtion:(.+?)(\s{4}\*Operation:.+)'
            case_name_setup = re.findall(case_pattern,case_detail,re.S)
            subcase['casename'] = case_name_setup[0][0].strip()
            subcase['setup'] = case_name_setup[0][1].strip()
            case_op_pattern = r'\s{4}\*Operation:(.+?)\s{4}\*Expect Result:(.+?)\s{4}\*Check Point:(.+?)\n'
            case_op = re.findall(case_op_pattern,case_name_setup[0][2]+'\n',re.S)
            for case_step in case_op:
                sub_step_list = filter(lambda x:x.strip(), case_step[0].strip().split('\n'))
                for sub_step in sub_step_list:
                    subcase['steps'].append((sub_step.strip(),[]))
                for sub_step in filter(lambda x:x.strip(), case_step[1].strip().split('\n')):
                    subcase['steps'].append(('Expect ' + sub_step,[]))
                for sub_step in filter(lambda x:x.strip(), case_step[2].strip().split('\n')):
                    subcase['steps'].append(('Check ' + sub_step,[]))
            self.case_list.append(subcase)
        return self.case_list
    

    def generate_keywords(self):
        self.keyword_list = []
        keywords_list = []
        for case in self.case_list:
            keywords_list.append(case['setup'])
            for case_step in case['steps']:
                keywords_list.append(case_step[0])

        for keyword in  set(filter(lambda x: x.strip(),keywords_list)):
            self.keyword_list.append({'keywordname':keyword})
        return self.keyword_list

    
    def write_case_content_to_file(self, file_name, content):
        with open(file_name,'w+') as f:
            f.write(content)


    def generate_robot_case(self):
        robot_documentation = 'Scope: ' + self.scope + '\nQuestions: '+self.question + '\nAssumpthion: '+self.assumption
        self.robot_case_content = SettingField(robot_documentation.replace('\n','\n...    ')).generate_setting_field()
        variable = {}
        self.robot_case_content += '\n'+ VariableField(**variable).generate_variable_field()
        testcases = self.generate_cases()
        self.robot_case_content += '\n' + TestCaseField(testcases).generate_case_field()
        keywords = self.generate_keywords()
        self.robot_case_content += '\n' + KeywordField(keywords).generate_keyword_field()
        self.write_case_content_to_file(self.robot_case_name,self.robot_case_content)
        return self.robot_case_name


     


if __name__ == '__main__':
    class TEST(object):
        def __init__(self):
            self.content = '''####Subcase: my first test sub case
    *Precondtion: condition is ok
    *Operation:do some action
    *Expect Result:expect true
      ADD the expect 
    *Check Point:check the result is ok''' 
            self.scope = "my first scope\n thans for scope"
            self.question = "first question \n question one"
            self.assumption = "assumption is ok for me"

    FILE_NAME = './first_grooming2robot.robot'
    GroomingAtddToRobot(TEST(),FILE_NAME).generate_robot_case()

  

