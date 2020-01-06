var errors = {
    'fileSize': 'La foto es muy grande ({{ value }} max).',
    'minWidth': 'Ancho de la foto muy pequeño ({{ value }}}px min).',
    'maxWidth': 'Foto demasiado ancha ({{ value }}}px max).',
    'minHeight': 'Foto demasiado baja ({{ value }}}px min).',
    'maxHeight': 'Foto demasiao alta ({{ value }}px max).',
    'imageFormat': 'Formato no permitido ({{ value }} permitidos).'
}

var image_one = $('#id_image_one').dropify({
    messages: {
        default: 'Agregar imagen principal',
        replace: 'Haz clic para reemplazar la imagen',
        remove:  'Quitar',
        error:   'Ooops! Algo salió mal'
    },
    error: errors
});
var image_two = $('#id_image_two').dropify({
    messages: {
        default: 'Agregar imagen',
        replace: 'Haz clic para reemplazar la imagen',
        remove:  'Quitar',
        error:   'Ooops! Algo salió mal'
    },
    error: errors
});
var image_three = $('#id_image_three').dropify({
    messages: {
        default: 'Agregar imagen',
        replace: 'Haz clic para reemplazar la imagen',
        remove:  'Quitar',
        error:   'Ooops! Algo salió mal'
    },
    error: errors
});

var image_four = $('#id_image_four').dropify({
    messages: {
        default: 'Agregar imagen',
        replace: 'Haz clic para reemplazar la imagen',
        remove:  'Quitar',
        error:   'Ooops! Algo salió mal'
    },
    error: errors
});

function editDropifyElement (event, element){
    let input = document.getElementById('id_images_status')
    let value = input.value // 0::0::0::0
    let splittedValue = value.split('::') // ['0', '0', '0'm '0']

    let eventName = event.target.name

    if (eventName == 'image_one') {
        splittedValue[0] = '1'
    } else if (eventName == 'image_two') {
        splittedValue[1] = '1'
    } else if (eventName == 'image_three') {
        splittedValue[2] = '1'
    } else if (eventName == 'image_four') {
        splittedValue[3] = '1'
    } 

    // Array to string '1::1::1::1'
    input.value = splittedValue.join('::')

}

image_one.on('dropify.afterClear', editDropifyElement);
image_two.on('dropify.afterClear', editDropifyElement);
image_three.on('dropify.afterClear', editDropifyElement);
image_four.on('dropify.afterClear', editDropifyElement);
