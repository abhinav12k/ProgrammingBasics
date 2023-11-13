import sys
import os

def isPathExists(path):
    return os.path.exists(path)

def get_file_path(input_prompt: str):
    print(input_prompt)
    file_path = input()
    if not isPathExists(file_path):
        print(f"Specified file path doesn't exist")
        sys.exit()
    return file_path

def to_snake_case(text):
    return text.replace(' ', '_').lower()

def to_camel_case(snake_str):
    return "".join(x.capitalize() for x in snake_str.lower().split("_"))

def get_widget_template_name(widget_name):
    widget_name_in_snake_case = to_snake_case(widget_name)
    expected_widget_template_name = widget_name_in_snake_case
    if widget_name_in_snake_case.find('widget') == -1:
        expected_widget_template_name = widget_name_in_snake_case+'_widget'
    return expected_widget_template_name

def get_widget_config_file_name(widget_template_name):
    return to_camel_case(widget_template_name)+'Config'

def get_widget_view_file_name(widget_template_name):
    return to_camel_case(widget_template_name)+'View'

def get_widget_file_name(widget_template_name):
    return to_camel_case(widget_template_name)

def get_widget_view_binder_file_name(widget_template_name):
    return to_camel_case(widget_template_name)+'ViewBinder'

def check_if_widget_already_present(file_path, template_name):
    with open(file_path,mode = 'r') as widget_types_file:
        for line in widget_types_file:
            try:
                foundIdx = line.find(template_name)
                if foundIdx != -1 and line[foundIdx+len(template_name)] == '"' and line[foundIdx-1] == '"':
                    return True
            except IndexError:
                pass
    return False

def update_widget_types_file(file_path, widget_template_name: str):
    widget_number = -3
    with open(file_path, mode= 'r') as rf:
        with open(file_path+'.tmp', mode='w') as wf:
            line = rf.readline()
            while line:
                widget_number = widget_number + 1
                if line.strip() == '}':
                    wf.seek(rf.tell()-2)
                    wf.write(',\n')
                    text_to_append = f'    {widget_template_name.upper()}("{widget_template_name}", {widget_number})\n'
                    wf.write(text_to_append)
                    wf.write('}')
                else:
                    wf.write(line)
                line = rf.readline()
    
    with open(file_path+'.tmp', mode = 'r') as rf:
        with open(file_path, mode = 'w') as wf:
            for line in rf:
                wf.write(line)
    
    os.remove(file_path+'.tmp')

def update_widget_config_deserializer_file(file_path, widget_template_name: str, widget_config_class_name: str):
    
    deserializer_statement = f'                    WidgetTypes.{widget_template_name.upper()}.type -> return context.deserialize(jsonObject, {widget_config_class_name}::class.java)'
    serializer_statement = f'                    WidgetTypes.{widget_template_name.upper()}.type -> jsonObject = context.serialize(src, {widget_config_class_name}::class.java)'

    deserializer_statement_written = False
    serializer_statement_written = False
    brackets = []
    with open(file_path, mode = 'r') as rf:
        with open(file_path+'.tmp', mode = 'w') as wf:
            for line in rf:
                if line.find('{') != -1:
                    brackets.append('{')
                elif line.find('}') != -1:
                    brackets.pop()

                if line.strip() == '}' and len(brackets) == 4 and not deserializer_statement_written:
                    deserializer_statement_written = True
                    wf.write(deserializer_statement+'\n')
                    wf.write('                }\n')
                elif line.strip() == '}' and len(brackets) == 5 and not serializer_statement_written:
                    serializer_statement_written = True
                    wf.write(serializer_statement+'\n')
                    wf.write('                }\n')
                else:
                    wf.write(line)

    with open(file_path+'.tmp', mode = 'r') as rf:
        with open(file_path, mode = 'w') as wf:
            for line in rf:
                wf.write(line)
    
    os.remove(file_path+'.tmp')

def create_widget_config_file(target_dir, filename, package_dir, widget_template_name):

    vars = {'filename':filename, 'widget_data':f"{filename.replace('Config','')}Data", 'package_dir':package_dir, 'widget_type':f"{widget_template_name.upper()}"}

    file_contents = '''package {package_dir}

import com.google.gson.annotations.SerializedName
import com.indwealth.common.WidgetTypes
import com.indwealth.core.indwidget.WidgetConfig

data class {filename}(
    @SerializedName("widget_properties")
    val widgetData: {widget_data} = null
) : WidgetConfig() {{
    override fun getType(): String {{
        return WidgetTypes.{widget_type}.type
    }}

    override fun getTypeInt(): Int {{
        return WidgetTypes.{widget_type}.typeInt
    }}

}}'''.format(**vars)
    
    with open(target_directory+'/'+filename+'.kt',mode = 'w') as wf:
        wf.write(file_contents)

def create_widget_view_file(target_directory, widget_view_file_name, package_dir, parent_class_name, widget_config_file_name):

    vars = {'widget_view_file_name':widget_view_file_name, 'parent_class_name':parent_class_name, 'widget_config_file_name': widget_config_file_name, 'package_dir':package_dir, 'widget_file_name': f"{widget_config_file_name.replace('Config','')}"}

    file_contents = '''package {package_dir}

import android.content.Context
import android.util.AttributeSet
import android.view.LayoutInflater
import android.widget.FrameLayout
import com.indwealth.core.indwidget.WidgetView
import com.indwealth.core.indwidget.updateSpacing

class {widget_view_file_name} @JvmOverloads constructor(
    context: Context,
    attrs: AttributeSet? = null,
    defStyleAttr: Int = 0
) : {parent_class_name}(context, attrs, defStyleAttr), WidgetView<{widget_config_file_name}> {{

    private val binding = View{widget_file_name}Binding.inflate(LayoutInflator.from(context))
    
    init {{
        addView(binding.root)
    }}

    override fun updateView(widgetConfig: {widget_config_file_name}) {{
        updateSpacing(widgetConfig)
    }}

    override fun updateViewWithPayload(widgetConfig: {widget_config_file_name}, payload: Any) {{
        if (payload is {widget_config_file_name}) {{
            updateView(payload)
        }}
    }}
}}
'''.format(**vars)
    
    with open(target_directory+'/'+widget_view_file_name+'.kt',mode = 'w') as wf:
        wf.write(file_contents)

def create_widget_file(target_directory, widget_file_name, package_directory, widget_config_file_name, widget_view_file_name, widget_template_name):

    vars = {'widget_file_name':widget_file_name, 'widget_view_file_name':widget_view_file_name, 'package_dir':package_directory, 'widget_type':f"{widget_template_name.upper()}", 'widget_config_file_name':widget_config_file_name}

    file_contents = '''package {package_dir}

import android.content.Context
import com.indwealth.common.WidgetTypes
import com.indwealth.core.indwidget.BaseWidget

class {widget_file_name}(context: Context) : BaseWidget<{widget_view_file_name}, {widget_config_file_name}>(context) {{

    override fun createView(context: Context): {widget_view_file_name} {{
        return {widget_view_file_name}(context)
    }}

    override fun getType(): String {{
        return WidgetTypes.{widget_type}.type
    }}
}}
'''.format(**vars)
    
    with open(target_directory+'/'+widget_file_name+'.kt',mode = 'w') as wf:
        wf.write(file_contents)

def create_widget_view_binder_file(target_directory, widget_view_binder_file_name, package_directory, widget_config_file_name, widget_file_name, widget_template_name):

    vars = {'widget_file_name':widget_file_name, 'package_dir':package_directory, 'widget_type':f"{widget_template_name.upper()}", 'widget_config_file_name':widget_config_file_name, 'widget_view_binder_file_name':widget_view_binder_file_name}

    file_contents = '''package {package_dir}

import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.indwealth.common.WidgetTypes
import com.indwealth.core.adapter.BaseViewBinder
import com.indwealth.core.indwidget.WidgetViewHolder

class {widget_view_binder_file_name} : BaseViewBinder<{widget_config_file_name}, WidgetViewHolder<{widget_file_name}>>({widget_config_file_name}::class.java) {{

    override fun createViewHolder(parent: ViewGroup): RecyclerView.ViewHolder {{
        return WidgetViewHolder({widget_file_name}(parent.context))
    }}

    override fun bindViewHolder(
        model: {widget_config_file_name},
        viewHolder: WidgetViewHolder<{widget_file_name}>
    ) {{
        viewHolder.widget.updateWidget(model)
    }}

    override fun getViewType(): Int {{
        return WidgetTypes.{widget_type}.typeInt
    }}

    override fun areItemsTheSame(
        oldItem: {widget_config_file_name},
        newItem: {widget_config_file_name}
    ): Boolean {{
        return oldItem.getId() == newItem.getId()
    }}

    override fun areContentsTheSame(
        oldItem: {widget_config_file_name},
        newItem: {widget_config_file_name}
    ): Boolean {{
        return oldItem == newItem
    }}

    override fun bindViewHolderWithPayload(
        model: {widget_config_file_name},
        viewHolder: WidgetViewHolder<{widget_file_name}>,
        payload: Any
    ) {{
        viewHolder.widget.updateWidgetWithPayload(model, payload)
    }}

    override fun getChangePayload(
        oldItem: {widget_config_file_name},
        newItem: {widget_config_file_name}
    ): Any {{
        return newItem
    }}
}}
'''.format(**vars)
    
    with open(target_directory+'/'+widget_view_binder_file_name+'.kt',mode = 'w') as wf:
        wf.write(file_contents)

def create_widget_view_xml(target_directory, widget_view_xml_name):

    file_contents = '''<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="wrap_content">

</androidx.constraintlayout.widget.ConstraintLayout>
'''

    with open(target_directory+'/view_'+widget_view_xml_name+'.xml',mode = 'w') as wf:
        wf.write(file_contents) 

## Starting IndWidget Creator

print('Starting IndWidgetCreator...')

print('Enter Widget Name (e.g Upi Widget / Upi / Title subtitle) - ')
widget_name = input()
widget_template_name = get_widget_template_name(widget_name)
widget_config_file_name = get_widget_config_file_name(widget_template_name)
widget_view_file_name = get_widget_view_file_name(widget_template_name)
widget_view_binder_file_name = get_widget_view_binder_file_name(widget_template_name)
widget_file_name = get_widget_file_name(widget_template_name)

widget_type_file_path = 'features/common/src/main/java/com/indwealth/common/WidgetTypes.kt'
widget_config_deserializer_file_path = 'app/src/main/java/com/indwealth/android/util/WidgetConfigDeserializer.kt'

## Specify the target directory where you want the files to be created
target_directory = 'features/common/src/main/java/com/indwealth/common/indwidget/paymentsWidgets'
package_directory = '.'.join(target_directory.split('java/')[1].split('/'))

## Specify the parent class for view
parent_class_for_view = 'FrameLayout'

if check_if_widget_already_present(widget_type_file_path, widget_template_name):
    print('Widget already present please try again with a different name!')
    sys.exit()

print('Setting up files...')

update_widget_types_file(widget_type_file_path, widget_template_name)
print('Updated WidgetTypes File')

update_widget_config_deserializer_file(widget_config_deserializer_file_path, widget_template_name, widget_config_file_name)
print('Updated WidgetConfigDeserializer File')

create_widget_config_file(target_directory, widget_config_file_name, package_directory, widget_template_name)
print('Created Widget Config file')

create_widget_view_file(target_directory, widget_view_file_name, package_directory, parent_class_for_view, widget_config_file_name)
print('Created Widget View file')

create_widget_file(target_directory, widget_file_name, package_directory, widget_config_file_name, widget_view_file_name, widget_template_name)
print('Created Widget file')

create_widget_view_binder_file(target_directory, widget_view_binder_file_name, package_directory, widget_config_file_name, widget_file_name, widget_template_name)
print('Created WidgetViewBinder file')

create_widget_view_xml(target_directory, widget_template_name.lower())
print('Created Widget View xml')

print('Finished generating files :)')
print("Don't forget to add the widget config to widget list usecase or any other equivalent place!")