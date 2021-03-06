define(['trumbowyg', 'util/form', 'page-config', 'util/rest', 'util/attachments', 'tagator'], function (_trumbowyg, _form, _pageConfig, _rest, _attachments) {
    'use strict';

    var _form2 = _interopRequireDefault(_form);

    var _rest2 = _interopRequireDefault(_rest);

    function _interopRequireDefault(obj) {
        return obj && obj.__esModule ? obj : {
            default: obj
        };
    }

    var $content = $('#content').trumbowyg({
        lang: _trumbowyg.locale,
        btnsDef: {
            upload: {
                ico: 'insertImage'
            }
        },
        btns: [['undo', 'redo'], ['formatting'], 'btnGrp-design', ['link'], ['upload'], 'btnGrp-justify', 'btnGrp-lists', ['foreColor', 'backColor'], ['preformatted'], ['horizontalRule'], ['fullscreen']],
        'plugins': {
            upload: {
                serverPath: '/files/image/',
                fileFieldName: 'image',
                urlPropertyName: 'url'
            }
        }
    });

    var getContent = function getContent($el) {
        return $el.data('trumbowyg').$ed.html();
    };
    var api = _pageConfig.articleId ? '/api/articles/' + _pageConfig.articleId + '/' : '/api/articles/';
    var action = _pageConfig.articleId ? 'patch' : 'post';

    var editForm = new _form2.default('#edit-form', api, action, !_pageConfig.articleId).payload(function (data) {
        return data.tags = !data.tags ? [] : data.tags.split(',');
    }).payload(function (data) {
        return data.content = getContent($content);
    }).payload(function (data) {
        return data.mentions !== undefined && (data.mentions = data.mentions.split(','));
    }).submitted(function (response) {
        return response.ok(function (_ref) {
            var url = _ref.url;
            return location.href = url;
        });
    });

    // File Uploads

    new _attachments.Upload({
        $button: '#attachments',
        $progress: '.progress .progress-bar',
        $fileBox: '#file-box',
        $form: '#edit-form',
        tmpl: 'file-item',
        $noFiles: '.no-files',
        initialAPI: _pageConfig.articleId ? '/api/articles/' + _pageConfig.articleId + '/attachments/' : undefined
    });

    // Tagify

    new _rest2.default('/api/tags/').get().ok(function (tags) {
        $('#tags').tagator({
            autocomplete: tags.map(function (item) {
                return item.name;
            }),
            showAllOptionsOnFocus: true
        });
    });

    if (!_pageConfig.articleId) {
        new _rest2.default('/api/user_nicknames/').get().ok(function (nicknames) {
            $('#mentions').tagator({
                autocomplete: nicknames,
                showAllOptionsOnFocus: true,
                allowAutocompleteOnly: true
            });
        });
    }
});
//# sourceMappingURL=../__maps__/articles/edit.js.map
