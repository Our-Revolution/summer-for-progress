var gulp = require('gulp'),
  sass = require('gulp-sass'),
  watch = require('gulp-watch'),
  minifycss = require('gulp-minify-css'),
  rename = require('gulp-rename'),
  gzip = require('gulp-gzip'),
  livereload = require('gulp-livereload'),
  autoprefixer = require('gulp-autoprefixer'),
  sourcemaps = require('gulp-sourcemaps'),
  changed = require('gulp-changed'),
  imagemin = require('gulp-imagemin');

var gzip_options = {
	threshold: '1kb',
	gzipOptions: {
		level: 9
	}
};

/* Compile Our Sass */
/* Compile SASS */
gulp.task('sass', function() {
  return gulp.src('summerforprogress/static/src/scss/main.scss')
  .pipe(sass().on('error', sass.logError))
  .pipe(sourcemaps.write())
  .pipe(autoprefixer({
      browsers: ['last 2 versions','iOS 7', 'iOS 8', 'ie 9-11', 'android >= 4.2'],
      cascade: false
  }))
  .pipe(gulp.dest('summerforprogress/static/dist/css'))
  .pipe(livereload())
  .pipe(minifycss())
  .pipe(rename({suffix: '.min'}))
  .pipe(gulp.dest('summerforprogress/static/dist/css'))
  .pipe(gzip(gzip_options))
  .pipe(gulp.dest('summerforprogress/static/dist/css'))
  .pipe(livereload());
});

/* Optimize Images */
gulp.task('images', function() {
  return gulp.src('summerforprogress/static/src/img/**')
    .pipe(changed('summerforprogress/static/dist/img/'))
    .pipe(imagemin())
    .pipe(gulp.dest('summerforprogress/static/dist/img/'))
});

/* Copy Fonts to Dist */
gulp.task('fonts', function() {
  return gulp.src('summerforprogress/static/src/fonts/**/*')
    .pipe(gulp.dest('summerforprogress/static/dist/fonts'))
})


/* Watch Files For Changes */
gulp.task('watch', function() {
	livereload.listen();
	gulp.watch('summerforprogress/static/src/scss/*.scss', ['sass']);

	/* Trigger a live reload on any Django template changes */
	gulp.watch('**/templates/*').on('change', livereload.changed);

});

gulp.task('default', ['sass', 'watch']);
gulp.task('build', ['sass','fonts', 'images']);
